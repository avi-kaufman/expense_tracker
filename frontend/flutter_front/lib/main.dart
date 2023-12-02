import 'package:flutter/material.dart';
import 'package:flutter_front/src/widgets/app_bar_widget.dart';
import 'src/widgets/nav_bar_widget.dart';
import 'src/screens/home_screen.dart';

void main() {
  runApp(ExpenseTrackerApp());
}

class ExpenseTrackerApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
          backgroundColor: Color(0XFF2A3439),
          drawer: NavBarWidget(),
          appBar: AppBarWidget(),
          floatingActionButton: FloatingActionButton(
            backgroundColor: Colors.black,
            foregroundColor: Colors.white,
            onPressed: () {},
            child: const Icon(Icons.add),
          ),
          body: const HomeScreen()),
      debugShowCheckedModeBanner: false,
    );
  }
}
