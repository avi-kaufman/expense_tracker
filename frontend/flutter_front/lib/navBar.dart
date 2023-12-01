import 'package:flutter/material.dart';

class NavBar extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Drawer(
      child: ListView(
        children: [
          UserAccountsDrawerHeader(
            accountName: Text('Avi Kaufman'),
            accountEmail: Text('avrikaufman@gmail.com'),
            currentAccountPicture: CircleAvatar(
              child: ClipOval(
                  child: Image.network(
                      'https://media.istockphoto.com/id/1483329842/photo/studio-portrait-of-attractive-woman-wearing-shirt-and-laughing-while-sitting-at-isolated-grey.jpg?s=1024x1024&w=is&k=20&c=rjIKwziuhLala9CK_jKGNDYYL7ow-6lSV6hEbypX-hM=',
                      width: 90,
                      height: 90,
                      fit: BoxFit.cover)),
            ),
            decoration: BoxDecoration(
                image: DecorationImage(
                    image: NetworkImage(
                        'https://media.istockphoto.com/id/517188688/photo/mountain-landscape.jpg?s=1024x1024&w=is&k=20&c=MB1-O5fjps0hVPd97fMIiEaisPMEn4XqVvQoJFKLRrQ='),
                    fit: BoxFit.cover)),
          ),
          ListTile(
            leading: Icon(Icons.analytics),
            title: Text('Analytics'),
            onTap: () => null,
          ),
          ListTile(
            leading: Icon(Icons.donut_large_sharp),
            title: Text('Budget'),
            onTap: () => null,
          ),
          Divider(),
          ListTile(
            leading: Icon(Icons.settings),
            title: Text('Settings'),
            onTap: () => null,
          ),
          ListTile(
            leading: Icon(Icons.description),
            title: Text('Policies'),
            onTap: () => null,
          ),
          ListTile(
            leading: Icon(Icons.exit_to_app),
            title: Text('Exit'),
            onTap: () => null,
          ),
        ],
      ),
    );
  }
}
