package 정적메서드은행예제;



import java.awt.image.BandCombineOp;

public class Bank {
    private static int count = 0 ; // 정적 멤버, 클래스 생성시 생성
    private int account; // 잔액표시 , 인스턴스 필드, 객체가 생성될 때 함께 생성 됨
    private  String bank; // 은행이름 , 인스턴스 필드

    public Bank (String name , int account ){
        count++; //계좌 개설 갯수 확인용, 정적 멤버, 생성자가 호출 될 때 값이 증가됨
        this.bank = name;
        this.account = account;
    }
    public   static  int getCount(){// 정적메서드
        return count;
    }
    public void setDeposit(final int dep){
        account += dep; // 잔액에 입금 금액을 더해서 잔액을 누적
        System.out.println(dep+"을 입금 했습니다.");
    }
    public void setWithdraw(final  int with){
        if (with > account){
            System.out.println("잔액이 부족합니다");
        }else  {
            account -= with;
        }
    }

    public String getBank() {
        return bank;
    }

    public int getAccount() {
        return account;
    }
}
