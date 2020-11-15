import { AfterViewInit, Component, ElementRef, OnInit, QueryList, ViewChildren } from '@angular/core';
import { Button } from 'src/app/shared/interfaces/button';
import { ModalTab } from 'src/app/shared/interfaces/modal-tab';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit, AfterViewInit {
  show = true;
  msg = 'Tu familia te dejo, hijo de puta';
  activeCards = false;
  openModal = false;
  name = '';
  dataTitle: ModalTab[];
  cardInv = true;
  cardFun = true;
  cardGoods = true;
  cardWork = true;
  endTurn: Button = {
    name: 'Fin de turno',
    innerName: 'endTurn'
  }
  portfolioBtn: Button = {
    name: 'Portafolio',
    innerName: 'portfolio'
  };
  portfolio: ModalTab[] = [
    {
      name: 'Portafolio',
      active: true,
      internalName: 'portfolio',
      position: 0
    }
  ]
  newActionsBtn: Button = {
    name: 'Bolsa',
    innerName: 'newActions',
  };
  newActions: ModalTab[] = [
    {
      name: 'Bolsa',
      active: true,
      internalName: 'newActions',
      position: 0
    }
  ]
  newLoanBtn: Button = {
    name: 'Préstamos',
    innerName: 'newLoan'
  };
  newLoan: ModalTab[] = [
    {
      name: 'Préstamos',
      active: true,
      internalName: 'newLoan',
      position: 0
    }
  ];
  myActionsBtn: Button = {
    name: 'Mis inversiones',
    innerName: 'myActions'
  };
  myActions: ModalTab[] = [
    {
      name: 'Bolsa',
      active: true,
      internalName: 'newActions',
      position: 0
    },
    {
      name: 'Personales',
      active: false,
      internalName: 'newActions',
      position: 1
    }
  ];
  myLoansBtn: Button = {
    name: 'Mis préstamos',
    innerName: 'myLoans'
  };
  myLoans: ModalTab[] = [
    {
      name: 'Mis préstamos',
      active: true,
      internalName: 'myLoans',
      position: 0
    }
  ];
  question: ModalTab[] = [
    {
      name: 'Preguntas',
      active: true,
      internalName: 'questions',
      position: 0
    }
  ];

  constructor() { }

  ngOnInit(): void {
  }
  ngAfterViewInit(): void {
    // setInterval(() => {this.updateGradient();}, 10);
  }
  close(action: boolean): void { // Notifications
    this.show = action;
  }
  openModalFun(activateModal: Button): void { // Modal
    switch(activateModal.innerName) {
      case 'portfolio': 
        this.dataTitle = this.portfolio;
        break;
      case 'newActions':
        this.dataTitle = this.newActions;
        break;
      case 'newLoan':
        this.dataTitle = this.newLoan;
        break;
      case 'myActions':
        this.dataTitle = this.myActions;
        break;
      case 'myLoans':
        this.dataTitle = this.myLoans;
        break;
    }
    this.openModal = true;
  }
  openModalCard(): void { 
    // TODO: receives descripction
    this.dataTitle = this.question;
    this.openModal = true;
  }

  blockOthers(name: string): void {
    switch(name) {
      case 'inv':
        this.cardFun = false;
        this.cardGoods = false;
        this.cardWork = false;
      break;
      case 'fun':
        this.cardInv = false;
        this.cardGoods = false;
        this.cardWork = false;
      break;
      case 'goods':
        this.cardInv = false;
        this.cardFun = false;
        this.cardWork = false;
      break;
      case 'work':
        this.cardInv = false;
        this.cardFun = false;
        this.cardGoods = false;
      break;
    }
  }
  resetCards(flag: boolean): void {
    this.cardInv = true;
    this.cardFun = true;
    this.cardWork = true;
    this.cardGoods = true;
    this.activeCards = flag;
  }
}

