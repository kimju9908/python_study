package 에어컨만들기;

import java.util.Calendar;
import java.util.Scanner;
import java.util.logging.Logger;

public class Aircon {
    private boolean isPower;// 전원 ON/OFF
    private int setTemp;// 온도 설정 기능
    private int curTemp;// 현재온도
    private boolean isCooler; // 에어컨 동작 여부
    private boolean isHeater;// 히터 동작 여부
    private  int windStep;// 바람세기: 1,2,3단

    public  Aircon(){//생성자에서 인스턴스의 초기값을 부여, 현재 온도를 부여
        // 현재온도를 가져 오기 위해서 Calendar 클래스를 이용해 현재가 몇월인지를 운영체제로 부터 가져와서
//       // 미리정해둔 온도 배열에서 온도 값을 가져 옴
        final int[] monthTmp = {-5,3,10,15,22,28,32,30,24,16,8,1};
        Calendar now = Calendar.getInstance();
        int month = now.get(Calendar.MONTH);// 배열의 인덱스와 동일
        curTemp = monthTmp[month]; //해당 월에 대한 온도를 가져 옴
        isPower = false;
        setTemp = 18;
        isCooler= false;
        isHeater = false;
        windStep = 1;
    }
    // 콘솔화면에 현재 에어컨 정보 출력하기
    // 온도가 바뀔 때 화면에 출력 되도록 구현
    void airConInfo(){
        String onOffStr =  (isPower) ?"ON":"OFF";
        String heaterStr =  (isPower) ?"ON":"OFF";
        String coolerStr =  (isPower) ?"ON":"OFF";
        final String[] windStr = {"","1단계","2단계","3단계"};
        System.out.println("=======에어컨 정봌=======");
        System.out.println("전원"+onOffStr);
        System.out.println("현재온도"+curTemp);
        System.out.println("설정온도"+setTemp);
        System.out.println("히털"+heaterStr);
        System.out.println("쿨러"+coolerStr);
        System.out.println("바람세기"+windStr[windStep]);



    }

    public void setAirConState (){
        Scanner sc = new Scanner(System.in);
        System.out.println("현재 온도가 "+curTemp+" 도 입니다");
        System.out.print("온도를 설정 하세요:");
        setTemp = sc.nextInt();
        System.out.println("설정온도는"+setTemp);
        System.out.println("바람 세기를 설정하세요:");
        windStep=sc.nextInt();

        if (curTemp>setTemp){
            System.out.println("colo가 작동합니다.");
            isCooler = true;
            isHeater = false;

        }else if (curTemp>setTemp){
            isCooler = false;
            isHeater =true;
        }else {
            isCooler = false;
            isHeater = false;
        }
    }

    public boolean isPower() {
        return isPower;
    }

    public int getSetTemp() {
        return setTemp;
    }

    public int getCurTemp() {
        return curTemp;
    }

    public boolean isCooler() {
        return isCooler;
    }

    public boolean isHeater() {
        return isHeater;
    }

    public int getWindStep() {
        return windStep;
    }

    public void setPower(boolean power) {
        isPower = power;
    }

    public void setSetTemp(int setTemp) {
        this.setTemp = setTemp;
    }

    public void setCurTemp(int n) {//현재 온도에서 입력된 값의 크기 만큼 변경해서 다시 대입 0
        this.curTemp += n;
    }

    public void setCooler(boolean cooler) {
        isCooler = cooler;
    }

    public void setHeater(boolean heater) {
        isHeater = heater;
    }

    public void setWindStep(int windStep) {
        this.windStep = windStep;
    }
}
