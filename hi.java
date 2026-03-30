public class helloWorldApp {
    public static void main(String[] args) {
        try {
            System.out.println("Hello World");
        } catch (Exception e) {
            java.util.logging.Logger.getLogger(helloWorldApp.class.getName()).log(java.util.logging.Level.SEVERE, null, e);
        }
    }
}