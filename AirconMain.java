package 에어컨만들기;

import java.util.Scanner;

import static java.lang.Thread.sleep;

public class AirconMain {
    public static void main(String[] args) throws InterruptedException {
        Aircon lgAirCon = new Aircon();
        Scanner sc= new Scanner(System.in);

        int elapsedTime = 0;// 경과시간 계산
        boolean isSetTemp = false; // 온도가 변경 될 상황인지 확인하는 조건
        System.out.println("에어컨을 켜시겠습니까?(yse/no): ");
        String isOn= sc.next();
        if(isOn.equalsIgnoreCase("yes")){
            lgAirCon.setPower(true);// 어에컨 켜기
            lgAirCon.setAirConState();// 온도설정과 바람세기 설정
            while (true){// 현재 온도와 설정 온도가 같을 때 까지 반복
                sleep(1000);
                elapsedTime++; // 1초마다 경과 시간 값이 1씩 증가
                switch (lgAirCon.getWindStep()){
                    case 1: if(elapsedTime >=60) isSetTemp = true; break;
                    case 2: if(elapsedTime>=30) isSetTemp = true; break;
                    case 3: if(elapsedTime>=20) isSetTemp = true; break;
                }
                if(isSetTemp){
                    if(lgAirCon.isHeater()) lgAirCon.setCurTemp(1);
                    if (lgAirCon.isCooler()) lgAirCon.setCurTemp(-1);
                    lgAirCon.airConInfo();
                    isSetTemp = false;
                    elapsedTime =0;
                }
                if(lgAirCon.getCurTemp()==lgAirCon.getSetTemp()){
                    System.out.println("에어컨을 종료 합니다.");
                    break;
                }
            }
        }
    }
}
