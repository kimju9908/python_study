package 싱글톤;
/*싱글톤: 단 하나의 객체만 생성하는 디자인 패턴
 장점: 메모리를 절약, 생성된 하나의 객체를 재활용해서 사용(스프링부트 빈 컨테이너에서 사용)
 클래스로 생성된 객체간의 정보 공유가 쉬움(안드로이드나 ios에서 사용되는 방식)
 단점: 동시성 문제가 발생 할 수 있음,
*/
public class SingletonEx {
    public static void main(String[] args) {
        Student student1 = new Student();
        Student student2 = new Student();
        student1.setInfo("김줗력",21); // 정보를 전달
        student2.viewInfo();

    }
}
