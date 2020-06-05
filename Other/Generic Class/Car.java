public class Car<T> {
    private String Make;
    private String Model;
    private int Year;
    private String Engine;
    private T EngineVolume;

    public Car(String Make, String Model, int Year, String Engine, T EngineVolume) {
        this.Make = Make;
        this.Model = Model;
        this.Year = Year;
        this.Engine = Engine;
        this.EngineVolume = EngineVolume;
    }

    public String getMake() { return this.Make; }
    public String getModel() { return this.Model; }
    public int getYear() { return this.Year; }
    public String getEngine() { return this.Engine; }
    public T getEngineVolume() { return this.EngineVolume; }Model

    public void setMake(String Make) { this.Make = Make;}
    public void setModel(String Model) { this.Model = Model;}
    public void setYear(int Year) { this.Year = Year;}
    public void setEngine(String Engine) { this.Engine = Engine;}
    public void setEngineVolume(T EngineVolume) { this.EngineVolume = EngineVolume;}
}