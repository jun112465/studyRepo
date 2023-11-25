# Jwt Login 기능 구현

## 클래스 구현 목록
- security
    - JwtAuthenticationFilter
    - JwtTokenProvider
    - SecurityConfig
- model
    - JwtToken
    - User
- controller
    - userController
- service 
    - userService
    - customUserService

## 로그인 과정 (인증)
1. Client Side에서 (id, pw) 정보를 담아 Request

2. userController
    ```java
    @PostMapping("/login")
    public String login(
        @RequestBody UserLoginRequestDto userLoginRequestDto, HttpServletResponse response) {
        String memberId = userLoginRequestDto.getUserId();
        String password = userLoginRequestDto.getPassword();

        JwtToken jwtToken = userService.login(memberId, password);

        // 쿠키 환경 설정 및 추가
        Cookie mySessionCookie = new Cookie("accessToken", jwtToken.getAccessToken());
        mySessionCookie.setMaxAge(30 * 24 * 60 * 60 * 1000);
        mySessionCookie.setHttpOnly(true);
        mySessionCookie.setPath("/");
        response.addCookie(mySessionCookie);

        return "main";
    }
    ```
    userService의 login() 메소드를 통해 jwtToken을 반환받음

3. userService
    ~~~java
    @Transactional
    public JwtToken login(String userId, String password){

        System.out.println("userService start");

        // 1. Login ID/PW 를 기반으로 Authentication 객체 생성
        // 이때 authentication 는 인증 여부를 확인하는 authenticated 값이 false
        UsernamePasswordAuthenticationToken authenticationToken = new UsernamePasswordAuthenticationToken(userId, password);
        log.info(authenticationToken.toString());

        // 2. 실제 검증 (사용자 비밀번호 체크)이 이루어지는 부분
        // authenticate 매서드가 실행될 때 CustomUserDetailsService 에서 만든 loadUserByUsername 메서드가 실행 (검증을 위해)
        Authentication authentication = authenticationManagerBuilder.getObject().authenticate(authenticationToken);
        log.info(authentication.toString());

        // 3. 인증 정보를 기반으로 JWT 토큰 생성
        JwtToken token = jwtTokenProvider.generateToken(authentication);
        log.info(token.toString());


        log.info("AccessToken : " + token.getAccessToken() + " , RefreshToken : " + token.getRefreshToken());
        return token;
    }
    ~~~

4. CustomUserDetailsService
    ```java
    @Override
        public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {

            return userRepository.findById(username)
                    .map(this::createUserDetails)
                    .orElseThrow(() -> new UsernameNotFoundException("해당하는 회원을 찾을 수 없습니다."));
        }

        // 해당하는 User 의 데이터가 존재한다면 UserDetails 객체로 만들어서 return
        private UserDetails createUserDetails(User user) {
            return User.builder()
                    .userId(user.getUsername())
                    .password(passwordEncoder.encode(user.getPassword()))
    //                .role(user.getRole())
                    .roles(user.getRoles())
                    .build();
        }
    ```
5. JwtTokenProvider
    ```java
    public JwtToken generateToken(Authentication authentication) {
            // 권한 가져오기
            String authorities = authentication.getAuthorities().stream()
                    .map(GrantedAuthority::getAuthority)
                    .collect(Collectors.joining(","));
            log.info(authorities);

            long now = (new Date()).getTime();

            // Access Token 생성
            Date accessTokenExpiresIn = new Date(now + 86400000); // 1 day
            String accessToken = Jwts.builder()
                    .setSubject(authentication.getName())
                    .claim("auth", authorities)
                    .setExpiration(accessTokenExpiresIn)
                    .signWith(key, SignatureAlgorithm.HS256)
                    .compact();

            // Refresh Token 생성
            String refreshToken = Jwts.builder()
                    .setExpiration(new Date(now + 86400000)) // 1 day
                    .signWith(key, SignatureAlgorithm.HS256)
                    .compact();

            return JwtToken.builder()
                    .grantType("Bearer")
                    .accessToken(accessToken)
                    .refreshToken(refreshToken)
                    .build();
        }
    ```

## 인가 과정 (Authorization)
1. Client에서 AccessToken값이 저장된 쿠키가 포함된 Request를 보냄
2. SecurityConfig
    ```java
    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
                .httpBasic().disable()
                .csrf().disable()
                .sessionManagement().sessionCreationPolicy(SessionCreationPolicy.STATELESS)
                .and()
                .authorizeRequests()
                .antMatchers("/").permitAll()
                .antMatchers("/users/login").permitAll()
                .antMatchers(HttpMethod.GET,"/users/login").permitAll()
                .antMatchers("/users/test").hasRole("USER")
                // recourses 에 대한 permission
                .requestMatchers(PathRequest.toStaticResources().atCommonLocations()).permitAll()
                .anyRequest().authenticated()
                .and()
                    //JWT 인증을 위하여 직접 구현한 필터를 UsernamePasswordAuthenticationFilter 전에 실행하겠다는 설정이다.
                    .addFilterBefore(new JwtAuthenticationFilter(jwtTokenProvider), UsernamePasswordAuthenticationFilter.class);

        return http.build();
    }
    ```
3. JwtAuthenticationFilter
    ```java
    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain) throws ServletException, IOException {

        // HTTP Only 쿠키에서 토큰 값을 가져오기
        Cookie[] cookies = request.getCookies();
        String accessToken = null;
        Optional<Cookie> accessTokenCookie = Arrays.stream(cookies).filter(cookie -> cookie.getName().equals("accessToken")).findFirst();
        if(accessTokenCookie.isPresent()) accessToken = accessTokenCookie.get().getValue();

        // 2. validateToken으로 토큰 유효성 검사
        if (accessToken != null && jwtTokenProvider.validateToken(accessToken)) {
            // 토큰이 유효할 경우 토큰에서 Authentication 객체를 가지고 와서 SecurityContext에 저장
            Authentication authentication = jwtTokenProvider.getAuthentication(accessToken);
            SecurityContextHolder.getContext().setAuthentication(authentication);
        }

        log.info(accessToken);

        filterChain.doFilter(request, response);
    }
    ```
4. JwtTokenProvider
    ```java
    public boolean validateToken(String token) {
        try {
            Jwts.parserBuilder()
                    .setSigningKey(key)
                    .build()
                    .parseClaimsJws(token);
            return true;
        } catch (SecurityException | MalformedJwtException e) {
            log.info("Invalid JWT Token", e);
        } catch (ExpiredJwtException e) {
            log.info("Expired JWT Token", e);
        } catch (UnsupportedJwtException e) {
            log.info("Unsupported JWT Token", e);
        } catch (IllegalArgumentException e) {
            log.info("JWT claims string is empty.", e);
        }
        return false;
    }
    ```
    ```java
    public Authentication getAuthentication(String accessToken) {
        // Jwt 토큰 복호화
        Claims claims = parseClaims(accessToken);

        if (claims.get("auth") == null) {
            throw new RuntimeException("권한 정보가 없는 토큰입니다.");
        }

        // 클레임에서 권한 정보 가져오기
        Collection<? extends GrantedAuthority> authorities = Arrays.stream(
                claims.get("auth").toString().split(","))
                .map(SimpleGrantedAuthority::new)
                .collect(Collectors.toList());

        // UserDetails 객체를 만들어서 Authentication return
        // UserDetails: interface, User: UserDetails를 구현한 class
        UserDetails principal = new User(claims.getSubject(), "", authorities);
        return new UsernamePasswordAuthenticationToken(principal, "", authorities);
    }
    ```
5. userController
    ```java
    @GetMapping("/get-current-member")
    @ResponseBody
    public String getCurrentMember(@AuthenticationPrincipal UserDetails userDetails){
        return userDetails.getUsername();
    }
    ```
> 참고 
https://gksdudrb922.tistory.com/217