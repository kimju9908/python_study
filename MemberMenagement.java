package 회원관리;
import java.util.Scanner;
public class MemberMenagement {
    public class Member {
        int age;
        char gender;
        int job;


        public void getAge () {
            while (true) {
                Scanner sc = new Scanner(System.in);
                System.out.print("나이를 입력하세요: ");
                int age = sc.nextInt();
                if (age < 0 || age > 100) {
                    System.out.print("나이를 다시 입력해주세요 ");
                } else
                    break;
                }

            }
            public char getGender(){
            return  gender;
        }
        public void getJob(){
            while (true) {
                Scanner sc = new Scanner(System.in);
                System.out.print("1.학생 2. 회사원 3. 주부 4. 무직");
                int job = sc.nextInt();



            }
        }


    }
    public static void main(String [] args){

    }
}
