import { Component, OnInit } from '@angular/core';
import { TestService } from 'src/app/services/test.service';

@Component({
  selector: 'app-test',
  templateUrl: './test.component.html',
  styleUrls: ['./test.component.scss']
})
export class TestComponent implements OnInit {

  dataEventos: any;

  constructor(private testService: TestService) { }

  ngOnInit(): void {
    this.getTest();
  }

  getTest(): void {
    this.testService.getEvent().subscribe(
      (resp) => {
        this.dataEventos = resp;
      },
      (error) => {
        console.log("Error", error);
      }
    )
  }

  putTest(): void {
    this.testService.putEvent(this.dataEventos).subscribe(
      (resp) => {
        console.log("todo chido ", resp);
      },
      (error) => {
        console.log("Error", error);
      }
    )
  }

}
