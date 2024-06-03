package com.example.frontend.ui;

import java.awt.Color;
import java.awt.GridLayout;

import javax.swing.BorderFactory;
import javax.swing.BoxLayout;
import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

public class MainFrame extends JFrame {

    public MainFrame() {
        setTitle("forex toolkit");
        setSize(1000, 600);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        // application icon
        ImageIcon icon = new ImageIcon(getClass().getResource("/fxtk.png"));
        setIconImage(icon.getImage());

        initUI();
    }

    private void initUI() {
        JPanel panel = new JPanel(new GridLayout(2, 2, 20, 10));
        JPanel leftPanel = new JPanel();
        leftPanel.setLayout(new BoxLayout(leftPanel, BoxLayout.Y_AXIS));
        leftPanel.setBorder(BorderFactory.createMatteBorder(0, 0, 0, 5, Color.BLACK));
        for (int i = 1; i <= 4; i++) {
            leftPanel.add(new JLabel("Item " + i));
        }

        JPanel rightPanel = new JPanel();
        rightPanel.setLayout(new BoxLayout(rightPanel, BoxLayout.Y_AXIS));
        leftPanel.setBorder(BorderFactory.createMatteBorder(0, 0, 0, 5, Color.BLACK));
        for (int i = 1; i <= 4; i++) {
            rightPanel.add(new JLabel("EURUSD "+ i));
        }

        panel.add(leftPanel);
        panel.add(rightPanel);

        add(panel);
    }
}
