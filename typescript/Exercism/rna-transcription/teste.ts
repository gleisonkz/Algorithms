export interface Command {
    Execute(): boolean
}

export interface Player {
    Move(commandKeyboard: string): boolean
}

class CommandPlayer implements Command {
    constructor(public name: string, private ruleFn: () => boolean, private actionFn: () => number) {

    }

    Execute(): boolean {
        const executed = this.ruleFn() ? this.actionFn() > -1 : false
        return executed
    }
}

class CommandNullObject implements Command {

    static Instance = new CommandNullObject()

    private constructor() {
        console.log()
    }

    Execute(): boolean {
        return false
    }
}

class PlayerSquare implements Player {
    private dic: { [key: string]: Command } = {}

    public X = 0
    public Y = 0

    private GetCommand(name: string): Command {
        const command = this.dic[name] || CommandNullObject.Instance
        return command
    }

    public AddCommand(commandPlayer: CommandPlayer): void {
        this.dic[commandPlayer.name] = commandPlayer
    }

    public Move(commandKeyboard: string): boolean {
        const command = this.GetCommand(commandKeyboard)
        const executed = command.Execute()
        return executed
    }
}

class PlayerProxy implements Player {

    constructor(private player: PlayerSquare) {
    }

    public Move(commandKeyboard: string): boolean {

        
        let numero2 = Number("1")
        
        let numero3 = parseInt("1")

        console.log('Before Move')
        const executed = this.player.Move(commandKeyboard)
        console.log('After Move')
        return executed



    }
}

class Factory {

    constructor(private producao: boolean) {
    }

    CreatePlayer(): Player {
        const player = this.ConfigPlayer(new PlayerSquare())
        return player
    }

    ConfigPlayer(player: PlayerSquare): Player {
        const maxWidthLength = 50
        const maxHeightLength = 50

        const upCommand = new CommandPlayer('Up', () => player.Y > 0, () => player.Y--)
        const downCommand = new CommandPlayer('Down', () => player.Y < maxHeightLength - 1, () => player.Y++)
        const leftCommand = new CommandPlayer('Left', () => player.X > 0, () => player.X--)
        const rightCommand = new CommandPlayer('Right', () => player.X < maxWidthLength - 1, () => player.X++)

        player.AddCommand(upCommand)
        player.AddCommand(downCommand)
        player.AddCommand(leftCommand)
        player.AddCommand(rightCommand)

        if (this.producao) {

            return player
        }

        return new PlayerProxy(player)
    }
}

export interface Printer {
    Imprimir: void
}

const objFactory = new Factory(true)
const objFactory2 = new Factory(false)
const player1 = objFactory.CreatePlayer()

const executed = player1.Move('Up')
const executed1 = player1.Move('Down')
const executed2 = player1.Move('X')