package 집주소;
import  java.util.Scanner;
public class Homeaddr {

    public static void main(String[] args) {
        while (true) {
            int [] b =new int [100];
            int cnt = 2;
            Scanner sc = new Scanner(System.in);
            System.out.println("주소를 입력하세요:");
            String str = sc.next();
            String arr[] = str.split("");
                    for (int i = 0; i <= arr.length - 1; i++) {
                        if (arr[i].equals("0")) {
                            cnt += 4;
                        } else if (arr[i].equals("1")) {
                            cnt += 2;
                        } else {
                            cnt += 3;
                        }
                        cnt=cnt + (arr.length - 1);
                         b[i] = cnt;
                    }


                }
            }



        }


