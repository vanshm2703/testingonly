/**
 * A simple Java program that prints "Hello World" to the console.
 */
public class HelloWorld {
    /**
     * The main entry point for the program.
     * 
     * @param commandLineArguments Command line arguments passed to the program.
     */
    public static void main(String[] commandLineArguments) {
        try {
            System.out.println("Hello World");
        } catch (Exception e) {
            System.err.println("An error occurred: " + e.getMessage());
        }
    }
}