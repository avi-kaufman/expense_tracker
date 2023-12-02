import 'package:flutter/material.dart';
import '../widgets/pie_chart_widget.dart';
import '../widgets/expense_card_widget.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.center,
        children: <Widget>[
          PieChartWidget(),
          const SizedBox(height: 20),
          const Text(
            'Last week expenses',
            style: TextStyle(color: Colors.white, fontSize: 20),
          ),
          Expanded(
            child: ListView(
              children: <Widget>[
                ExpenseCard(),
                ExpenseCard(),
                ExpenseCard(),
                ExpenseCard(),
                ExpenseCard(),
                ExpenseCard(),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
