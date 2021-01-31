# Quantum Poker

This game is inspired by poker, with a quantum flavour! This game requires 3 players. Each player is assigned a qubit in the quantum circuit, and the objective of the game is to make sure that your qubit is in the $\vert 1 \rangle$ state upon measurement!

## Card Deck
In this game, the cards are quantum gates themselves! There are a total of 12 cards and they are:
* 1 SWAP gate,
* 1 Toffoli gate,
* 1 Hadamard gate,
* 3 Pauli X-gates,
* 3 CNOT gates,
* 3 Measure gates.

The cards can be used on the quantum circuit, applying a gate on it with the respective control and target qubits specified by the players.
  
## Gameplay
1. In the beginning, the quantum citcuit is initialised as such:
![](figures/initial_circuit.png)
2. Before the round begins, each player is given a Measure gate. Then the rest of the cards are shuffled and split among all players equally. 
3. The players can only see their own cards. 
4. At each player's turn, the player must use one card, specifying the card's control and target, when applicable.
5. The corresponding gate on the card will be applied onto the circuit above.
6. The circuit is visible to all players at all times.
7. When all players has taken their turn to put down their cards, the round ends.
8. All cards can be used at any round, except for the Measure card. The Measure card can only be used after the end of the first round.
9. The game ends when all players run out of cards, or when a Measure card is put down.

## How to Win

## Future Work