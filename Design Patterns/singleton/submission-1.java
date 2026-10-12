static class Singleton {

    private static Singleton uniqueInstance = null;
    private String mode = null;

    private Singleton() {
    }

    public static Singleton getInstance() {
        if (uniqueInstance == null) {
            uniqueInstance = new Singleton();
        }
        return uniqueInstance;
    }

    public String getValue() {
        return mode;
    }

    public void setValue(String value) {
        this.mode = value;
    }
    
}
