package 싱글톤;

public class Singleton {
    String name;
    int id;
    // 정적 변수 Singleton클래스에 대한 참조 변수 =>
    private static Singleton singleton = new Singleton();
    private Singleton (){
        name = "김주혁";
        id= 100;

    }
    static  Singleton getSingleton(){
        return singleton;
    }
}
