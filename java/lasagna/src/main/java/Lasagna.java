public class Lasagna {

    private final int EXPECTED_MINUTES = 40;
    private final int MINUTES_PER_LAYER = 2;

    public int expectedMinutesInOven() {
        return EXPECTED_MINUTES;
    }

    public int remainingMinutesInOven(int elapsedMinutes) {
        return EXPECTED_MINUTES - elapsedMinutes;
    }

    public int preparationTimeInMinutes(int numOfLayers) {
        return numOfLayers * MINUTES_PER_LAYER;
    }

    public int totalTimeInMinutes(int numOfLayers, int elapsedMinutes) {
        return elapsedMinutes + this.preparationTimeInMinutes(numOfLayers);
    }

}
