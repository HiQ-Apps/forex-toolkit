package com.example.frontend;

import javax.swing.SwingUtilities;

import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ConfigurableApplicationContext;

import com.example.frontend.UI.MainFrame;


@SpringBootApplication
public class FrontendApplication implements CommandLineRunner {

	public static void main(String[] args) {
		// have to set headless for now since no keyboard and mouse detected
		System.setProperty("java.awt.headless", "false");
		ConfigurableApplicationContext ctx = SpringApplication.run(FrontendApplication.class, args);
		SwingUtilities.invokeLater(() -> {
			MainFrame mainFrame = ctx.getBean(MainFrame.class);
			mainFrame.setVisible(true);
		});
		SpringApplication.run(FrontendApplication.class, args);
	}

	@Override
	public void run(String...args) throws Exception {
		// tasks to run on startup
	}
}
