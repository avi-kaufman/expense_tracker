import 'package:flutter/material.dart';

void main() {
  runApp(ExpenseTrackerApp());
}

class ExpenseTrackerApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
          appBar: AppBar(
            backgroundColor: Colors.black,
            centerTitle: true,
            title: const Text(
              'Expense Tracker',
              style: TextStyle(color: Colors.white, fontSize: 24),
            ),
            leading: IconButton(
              icon: const Icon(
                Icons.menu,
                color: Colors.white,
              ),
              tooltip: 'Shows the menu',
              onPressed: () {},
            ),
            actions: <Widget>[
              IconButton(
                  onPressed: () {},
                  icon: const Icon(
                    Icons.home,
                    color: Colors.white,
                  ))
            ],
          ),
          floatingActionButton: FloatingActionButton(
            backgroundColor: Colors.black,
            foregroundColor: Colors.white,
            onPressed: () {},
            child: const Icon(Icons.add),
          ),
          body: HomeScreen()),
      debugShowCheckedModeBanner: false,
    );
  }
}

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return const Column(
      crossAxisAlignment: CrossAxisAlignment.center,
      children: <Widget>[
        Card(
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: <Widget>[
              ListTile(
                leading: Icon(Icons.restaurant_menu, size: 45),
                title: Text('Food'),
                subtitle: Text('100 \$'),
              ),
            ],
          ),
        ),
        Card(
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: <Widget>[
              ListTile(
                leading: Icon(Icons.car_crash, size: 45),
                title: Text('Car'),
                subtitle: Text('250 \$'),
              ),
            ],
          ),
        )
      ],
    );
  }
}
