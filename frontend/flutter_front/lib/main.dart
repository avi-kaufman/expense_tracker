import 'package:flutter/material.dart';
import 'package:pie_chart/pie_chart.dart';
import './navBar.dart';

void main() {
  runApp(ExpenseTrackerApp());
}

class ExpenseTrackerApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
          backgroundColor: Color(0XFF2A3439),
          drawer: NavBar(),
          appBar: AppBar(
            backgroundColor: const Color(0XFF2F4F4F),
            centerTitle: true,
            title: const Text(
              'Expense Tracker',
              style: TextStyle(color: Colors.white, fontSize: 24),
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
          body: const HomeScreen()),
      debugShowCheckedModeBanner: false,
    );
  }
}

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
        margin: const EdgeInsets.fromLTRB(20, 20, 30, 0),
        child: const Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          children: <Widget>[
            SizedBox(height: 20),
            PieChart(
              centerText: 'Monthly sepent\n 100\$',
              dataMap: {'Food': 3, 'Car': 8, 'Denis': 15},
              chartType: ChartType.ring,
              colorList: [
                Color(0XFFD4AF37),
                Color(0XFFC0C0C0),
                Color(0XFFCD7F32),
                Color(0XFF333333),
                Color(0XFF4682B4)
              ],
              chartValuesOptions: ChartValuesOptions(
                showChartValuesInPercentage: true,
              ),
              // totalValue: 50.0,
            ),
            SizedBox(height: 20),
            Card(
              color: Color(0XFF43464B),
              child: Column(
                mainAxisSize: MainAxisSize.min,
                children: <Widget>[
                  ListTile(
                    leading: Icon(
                      Icons.restaurant_sharp,
                      size: 45,
                      color: Colors.white,
                    ),
                    title: Text(
                      'Food',
                      style: TextStyle(color: Colors.white),
                    ),
                    subtitle: Text(
                      '327.80 \$',
                      style: TextStyle(color: Colors.white),
                    ),
                  ),
                ],
              ),
            ),
            Card(
              color: Color(0XFF43464B),
              child: Column(
                mainAxisSize: MainAxisSize.min,
                children: <Widget>[
                  ListTile(
                    leading: Icon(
                      Icons.car_crash,
                      size: 45,
                      color: Colors.white,
                    ),
                    title: Text(
                      'Car',
                      style: TextStyle(color: Colors.white),
                    ),
                    subtitle: Text(
                      '250 \$',
                      style: TextStyle(color: Colors.white),
                    ),
                  ),
                ],
              ),
            )
          ],
        ));
  }
}
