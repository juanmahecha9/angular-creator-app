def appComponentTs(pwd):
    file = open(f"{pwd}/src/app/app.component.ts", "w")
    file.write('''import { Component, OnInit } from "@angular/core";

@Component({
  selector: "teleperformance-rpa-root",
  templateUrl: "./app.component.html",
  styleUrls: ["./app.component.scss"],
})
export class AppComponent implements OnInit {
  title = "Intelligent Automation";

  ngOnInit(): void {
    console.log(
      `%c${this.title}`,
      "color: #0099ff; font-size: 40px; font-weight: bold;"
    );
    console.log(
      "%cSingle-page application, RPA",
      "color: red; font-size: 15px; font-weight: bold;"
    );
  }
}
'''
               )
    file.close()

