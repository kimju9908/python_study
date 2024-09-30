package 접근제한자;
// 접근제한자: 클래스와 인터페이스를 다른 패키지나 클래스에서의 접근을 제한하는 용도
public class CapsuleEX {
    public static void main(String[] args) {
        Child child = new Child("개발자");
        System.out.println(child.getJob());
        System.out.println(child.getMoney());
        System.out.println(child.getName());
        System.out.println(child.getAddr());

    }
}
class  Child extends Parent {

    String job;
    public Child(String jon){
    this.job = job;
}



    public String getJob() {
        return job;
    }
    public String getName() {
        return name;
    }

    public String getMoney() {
        return money;
    }
    public  String getAddr(){
        return addr;
    }


}
