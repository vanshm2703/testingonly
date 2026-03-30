public class HelloWorldApp extends Application {
    public static void main(String[] args) {
        if (args == null || args.length == 0) {
            System.out.println("No arguments provided.");
        } else {
            try {
                System.out.println("Hello World");
            } catch (Exception e) {
                System.out.println("An error occurred: " + e.getMessage());
            }
        }
    }
}