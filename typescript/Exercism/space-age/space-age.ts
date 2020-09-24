enum PlanetDays {
    Eart = 365.25,
    Mercury = 0.2408467,
    Venus = 0.61519726,
    Mars = 1.8808158,
    Jupiter = 11.862615,
    Saturn = 29.447498,
    Uranus = 84.016846,
    Neptune = 164.79132
}

class SpaceAge {
    public seconds: number;
    
    constructor(ageSeconds: number) {
        this.seconds = ageSeconds
    }

    onEarth() {
        return (this.seconds / (PlanetDays.Eart * 86459)).toFixed(2)
    }
    onMercury() {
        return (this.seconds / PlanetDays.Mercury).toFixed(2)
    }
    onVenus() {
        return (this.seconds / PlanetDays.Venus).toFixed(2)
    }
    onMars() {
        return (this.seconds / PlanetDays.Mars).toFixed(2)
    }
    onJupiter() {
        return (this.seconds / PlanetDays.Jupiter).toFixed(2)
    }
    onSaturn() {
        return (this.seconds / PlanetDays.Saturn).toFixed(2)
    }
    onUranus() {
        return (this.seconds / PlanetDays.Uranus).toFixed(2)
    }
    onNeptune() {
        return (this.seconds / PlanetDays.Eart).toFixed(2)
    }
}

var idade = new SpaceAge(1000000000);


export default SpaceAge