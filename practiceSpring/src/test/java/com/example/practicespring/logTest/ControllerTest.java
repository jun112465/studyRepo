package com.example.practicespring.logTest;


import com.example.practicespring.FooController;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
public class ControllerTest {

    @Autowired
    FooController fc;

    @Test
    public void test0(){
        fc.log();
    }
}
