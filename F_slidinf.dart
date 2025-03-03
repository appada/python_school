import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: '15-퍼즐 게임',
      theme: ThemeData.dark(),
      home: PuzzleGame(),
    );
  }
}

class PuzzleGame extends StatefulWidget {
  @override
  _PuzzleGameState createState() => _PuzzleGameState();
}

class _PuzzleGameState extends State<PuzzleGame> {
  List<int?> numbers = List.generate(16, (index) => index + 1)
    ..removeLast()
    ..add(null);

  @override
  void initState() {
    super.initState();
    newGame();
  }

  void newGame() {
    setState(() {
      numbers.shuffle();
    });
  }

  void onTileClick(int index) {
    //if (!canMove(index)) return;
    final emptyIndex = numbers.indexOf(null);
    if (((index % 4 - emptyIndex % 4).abs() + (index ~/ 4 - emptyIndex ~/ 4).abs()) == 1) {
      setState(() {
        final emptyIndex = numbers.indexOf(null);
        numbers[emptyIndex] = numbers[index];
        numbers[index] = null;
      });

      if (isGameWon()) {
        showWinDialog();
      }
    }
  }

  bool isGameWon() {
    for (int i = 0; i < 15; i++) {
      if (numbers[i] != i + 1) return false;
    }
    return numbers[15] == null;
  }

  void showWinDialog() {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: Text('축하합니다!'),
          content: Text('퍼즐을 완성했습니다!'),
          actions: <Widget>[
            TextButton(
              child: Text('확인'),
              onPressed: () {
                Navigator.of(context).pop();
              },
            ),
          ],
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('15-퍼즐 게임')),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Container(
              width: 300,
              height: 300,
              child: GridView.builder(
                gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
                  crossAxisCount: 4,
                  childAspectRatio: 1.0,
                  crossAxisSpacing: 5,
                  mainAxisSpacing: 5,
                ),
                itemCount: 16,
                itemBuilder: (context, index) {
                  return numbers[index] != null
                      ? MaterialButton(
                          child: Text('${numbers[index]}', style: TextStyle(fontSize: 24)),
                          onPressed: () => onTileClick(index),
                          color: Colors.blue[200],
                          shape: RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(10),
                          ),
                        )
                      : Container();
                },
              ),
            ),
            SizedBox(height: 20),
            ElevatedButton(
              child: Text('새 게임'),
              onPressed: newGame,
            ),
          ],
        ),
      ),
    );
  }
}
