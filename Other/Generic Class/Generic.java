public class Generic<T> {
    
    private T t;

    //Constructor
    public Generic(T t) {
        this.t = t;
    }

    //Get method
    public T get() {
        return t;
    }
    
    public static void main(String[] Args) {
        Generic<String> strReturner = new Generic<String>("What's up?");
        Generic<Integer> intReturner = new Generic<Integer>(505);

        System.out.println(strReturner.get());
        System.out.println(intReturner.get());
    }
}