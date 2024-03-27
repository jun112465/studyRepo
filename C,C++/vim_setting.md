1. vundle, clang, python3 설치 
2. '.vimrc' 파일 만들기
3. 아래와 같이 vimrc 파일 작성하기.
```
" Vundle 플러그인 매니저 사용 설정
set nocompatible              " Vim 표준 호환성 비활성화
filetype off                  " 파일 유형을 불러오지 않도록 설정
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

" 플러그인 목록
Plugin 'VundleVim/Vundle.vim'         " Vundle 플러그인 매니저
Plugin 'Valloric/YouCompleteMe'       " 코드 완성 플러그인
Plugin 'scrooloose/nerdtree'          " 파일 탐색기
Plugin 'airblade/vim-gitgutter'       " Git 상태 표시
Plugin 'scrooloose/syntastic'         " 구문 검사 및 정적 분석
Plugin 'tpope/vim-fugitive'           " Git 플러그인
Plugin 'jiangmiao/auto-pairs'         " 자동 괄호 완성
Plugin 'vim-airline/vim-airline'      " 상태 표시 줄
Plugin 'vim-airline/vim-airline-themes'  " 상태 표시 줄 테마
Plugin 'pangloss/vim-javascript'      " JavaScript 문법 강조
Plugin 'derekwyatt/vim-scala'         " Scala 문법 강조
Plugin 'plasticboy/vim-markdown'      " Markdown 문법 강조

call vundle#end()            " Vundle 종료
filetype plugin indent on    " 파일 유형 관련 플러그인 및 자동 들여쓰기 활성화

" YouCompleteMe 설정
let g:ycm_global_ycm_extra_conf = '~/.vim/bundle/YouCompleteMe/.ycm_extra_conf.py'

" NERDTree 설정
map <F2> :NERDTreeToggle<CR>          " F2 키로 NERDTree 토글

" GitGutter 설정
let g:gitgutter_sign_added = '+'      " 추가된 줄 표시 설정
let g:gitgutter_sign_modified = '~'   " 수정된 줄 표시 설정
let g:gitgutter_sign_removed = '-'    " 제거된 줄 표시 설정

" Syntastic 설정
let g:syntastic_enable_signs = 1      " 구문 오류 표시 활성화
let g:syntastic_always_populate_loc_list = 1  " 항상 오류 목록 채우기

" Auto-Pairs 설정
let g:auto_pairs_skip_wrapping = '^[^[:word:][:blank:]]*$'  " 괄호 자동 완성 제외 문자

" Airline 설정
let g:airline#extensions#tabline#enabled = 1  " 탭 라인 활성화
let g:airline#extensions#tabline#fnamemod = ':t'  " 탭 이름 축소 설정

" 자동 저장 설정
set autowrite

" 들여쓰기 설정
set tabstop=4
set shiftwidth=4
set expandtab

" 구문 강조 사용
syntax enable

" 색상 스킴 설정
colorscheme desert

" 상태바 설정
set laststatus=2
set statusline=%F%m%r%h%w%=[Line:%l/%L][Col:%c][%p%%]

" 마우스 설정
set mouse=a

" 파일 인코딩 설정
set encoding=utf-8
set fileencoding=utf-8

" 줄번호 설정
set number

" 매칭된 괄호 하이라이트 설정
set showmatch

" 줄 끝에 공백 표시 설정
set listchars=trail:·

" 키 매핑
map <F5> :!clear && gcc % -o %< && ./%<<CR>   " F5 키로 컴파일 후 실행

" 편집 창 분할시 커서 이동 설정
set splitbelow
set splitright

" 컬러링 세팅
set term=xterm-256color

" 자동 들여쓰기 활성화
filetype plugin indent on
```
4. :PluginInstall
5. YouCompleteMe 플러그인 컴파일
```
cd ~/.vim/bundle/YouCompleteMe
python3 install.py --clang-completer 

# 위 코드에서 에러가 뜨면
# --force-sudo 옵션 추가하기.
```
# 유용한 플러그인 정리
- [nerdtree] : https://github.com/preservim/nerdtree
- [syntastic] : https://github.com/vim-syntastic/syntastic?tab=readme-ov-file#installation
- [youCompleteMe] : https://github.com/ycm-core/YouCompleteMe?tab=readme-ov-file#installation
- 
# color schema setting
1. ~/.vim/colors 디렉토리 만들기
2. https://github.com/rafi/awesome-vim-colorschemes 해당 링크에서 colors 폴더 내부 내용 다운 받아 colors안에 저장하기. 1번을 건너뛰고 ~/.vim 디렉토리 하위에 colors를 저장해도 된다.
3. ~/.vimrc 설정해주기
   ```
   colo = colo onehalfdark
   ```
