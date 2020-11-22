import { Component, Input, OnInit, OnChanges, SimpleChanges } from '@angular/core';

@Component({
  selector: 'app-loader',
  templateUrl: './loader.component.html',
  styleUrls: ['./loader.component.scss']
})
export class LoaderComponent implements OnInit {
  @Input() value: number;
  radius = 54;
  circumference = 2 * Math.PI * this.radius;
  dashoffset: number;
  colorProgress = '';
  constructor() { 
    this.progress(0);
  }

  ngOnInit(): void {
  }
  ngOnChanges(changes: SimpleChanges) {
    if (changes.value.currentValue !== changes.value.previousValue) {
      this.progress(changes.value.currentValue);
      this.identifyHappiness();
    }
  }
  private progress(value: number) {
    const progress = value / 100;
    this.dashoffset = this.circumference * (1 - progress);
  }
  setMyStyles(): any {
    const styles = {
      'transform': 'translateX(-' + this.identifyHappiness() + '%)',
    };
    return styles;
  }
  identifyHappiness(): string {
    if (this.value >= 0 && this.value <= 15) { // Cara preocupada
      this.colorProgress = '#F51432';
      return '500';
    }
    if (this.value > 15 && this.value <= 30) { // Muy triste
      this.colorProgress = '#E9B80F';
      return '400';
    }
    if (this.value > 30 && this.value <= 45) { // Triste
      this.colorProgress = '#48E1E5';
      return '300';
    }
    if (this.value > 45 && this.value <= 65) { // Normal
      this.colorProgress = '#25C462';
      return '0';
    }
    if (this.value > 65 && this.value <= 82) { // Feliz
      this.colorProgress = '#04D017';
      return '100';
    }
    if (this.value > 82 && this.value <= 100) { // Muy feliz
      this.colorProgress = '#2CDA01';
      return '200';
    }
  }
}
