public class Strings {
    public static void main(String[] args) {
        // String concatenation
        String firstName = "John";
        String lastName = "Doe";
        String fullName = firstName + " " + lastName;
        System.out.println(fullName);

        // String length
        String txt = "Hello World";
        System.out.println("The length of the text string is: " + txt.length());

        // String uppercase and lowercase
        String txt2 = "Hello World";
        System.out.println(txt2.toUpperCase());
        System.out.println(txt2.toLowerCase());

        // String search
        String txt3 = "Please locate where 'locate' occurs!";
        System.out.println(txt3.indexOf("locate"));

        // String concatenation
        String firstName2 = "John ";
        String lastName2 = "Doe";
        System.out.println(firstName2.concat(lastName2));

        // String escape characters
        String txt4 = "We are the so-called \"Vikings\" from the north.";
        System.out.println(txt4);

        // String special characters
        String txt5 = "Hello\nWorld!";
        System.out.println(txt5);

        // String comparison
        String txt6 = "Hello";
        String txt7 = "Hello";
        System.out.println(txt6.equals(txt7));
    }
}
