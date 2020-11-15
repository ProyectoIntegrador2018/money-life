import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-digits-show',
  templateUrl: './digits-show.component.html',
  styleUrls: ['./digits-show.component.scss']
})
export class DigitsShowComponent implements OnInit {
  @Input() name: string;

  constructor() { }

  ngOnInit(): void {
  }
  num = Math.random() * 100000;

  pad(n: any, width: any, z: any): any {
    z = z || '0';
    n = n + '';
    return n.length >= width ? n : new Array(width - n.length + 1).join(z) + n;
  }

  // setTimeout(_: any => {
  //   $('.cou-item').find('ul').each(function(i, el){
  //     const val = this.pad(this.num, 5, 0).split("");
  //     const $el = $(this);
  //     $el.removeClass();
  //     $el.addClass('goto-' + val[i]);
  //   })
  // }, 1000);
  
  // setTimeout(_ => {
  //   this.counter();
  // }, 2500)
  
  // counter(): void {
  //   setInterval(_ => {
  //     $('.cou-item').find('ul').each(function(i, el){
  //       this.num += 1;
  //       var val = pad(this.num, 5, 0).split("");
  //       var $el = $(this);
  //       $el.removeClass();
  //       $el.addClass('goto-' + val[i]);
  //     })
  //   }, 250);
  // }

}
