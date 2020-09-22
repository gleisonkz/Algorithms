"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
class CommandPlayer {
    constructor(name, ruleFn, actionFn) {
        this.name = name;
        this.ruleFn = ruleFn;
        this.actionFn = actionFn;
    }
    Execute() {
        const executed = this.ruleFn() ? this.actionFn() > -1 : false;
        return executed;
    }
}
class CommandNullObject {
    constructor() {
        console.log();
    }
    Execute() {
        return false;
    }
}
CommandNullObject.Instance = new CommandNullObject();
class PlayerSquare {
    constructor() {
        this.dic = {};
        this.X = 0;
        this.Y = 0;
    }
    GetCommand(name) {
        const command = this.dic[name] || CommandNullObject.Instance;
        return command;
    }
    AddCommand(commandPlayer) {
        this.dic[commandPlayer.name] = commandPlayer;
    }
    Move(commandKeyboard) {
        const command = this.GetCommand(commandKeyboard);
        const executed = command.Execute();
        return executed;
    }
}
class PlayerProxy {
    constructor(player) {
        this.player = player;
    }
    Move(commandKeyboard) {
        console.log('Before Move');
        const executed = this.player.Move(commandKeyboard);
        console.log('After Move');
        return executed;
    }
}
class Factory {
    constructor(producao) {
        this.producao = producao;
    }
    CreatePlayer() {
        const player = this.ConfigPlayer(new PlayerSquare());
        return player;
    }
    ConfigPlayer(player) {
        const maxWidthLength = 50;
        const maxHeightLength = 50;
        const upCommand = new CommandPlayer('Up', () => player.Y > 0, () => player.Y--);
        const downCommand = new CommandPlayer('Down', () => player.Y < maxHeightLength - 1, () => player.Y++);
        const leftCommand = new CommandPlayer('Left', () => player.X > 0, () => player.X--);
        const rightCommand = new CommandPlayer('Right', () => player.X < maxWidthLength - 1, () => player.X++);
        player.AddCommand(upCommand);
        player.AddCommand(downCommand);
        player.AddCommand(leftCommand);
        player.AddCommand(rightCommand);
        if (this.producao) {
            return player;
        }
        return new PlayerProxy(player);
    }
}
const objFactory = new Factory(true);
const objFactory2 = new Factory(false);
const player1 = objFactory.CreatePlayer();
const executed = player1.Move('Up');
const executed1 = player1.Move('Down');
const executed2 = player1.Move('X');
//# sourceMappingURL=teste.js.map