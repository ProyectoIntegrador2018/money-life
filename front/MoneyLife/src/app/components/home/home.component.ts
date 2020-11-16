import { Component, OnInit } from '@angular/core';
import { KeysDataUser } from 'src/app/auth/keys-data';
import { Router } from '@angular/router';
/** Services */
import { EventService } from 'src/app/events-news/services/event.service';
import { QuestionsService } from 'src/app/flip-card/services/questions.service';
import { LoanService } from 'src/app/loan/services/loan.service';
import { ActionsService } from '../services/actions.service';
import { InitTurnService } from '../services/turn.service';
/** Interfaces */
import { Button } from 'src/app/shared/interfaces/button';
import { ModalTab } from 'src/app/shared/interfaces/modal-tab';
import { InitEvent } from 'src/app/events-news/interfaces/init-event';
import { Turn } from 'src/app/components/interfaces/turn';
import { InitQuestion } from 'src/app/flip-card/interfaces/init-question';
import { SharesStock } from 'src/app/components/interfaces/shares-stock';
import { Loans } from 'src/app/loan/interfaces/loans';
import { MyInvestments } from 'src/app/components/interfaces/my-investments';
import { PersonalInvestments } from 'src/app/components/interfaces/personal-investments';
import { MyLoans } from 'src/app/loan/interfaces/my-loans';
import { Portfolio } from 'src/app/components/interfaces/portfolio';
import { ModalResponse } from 'src/app/shared/interfaces/modal-response';


@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {
  show = true;
  activeCards = false;
  openModal = false;
  name = '';
  dataTitle: ModalTab[];
  dataModal: any[];
  cardInv = true;
  cardFun = true;
  cardGoods = true;
  cardWork = true;
  eventMicro: InitEvent;
  eventMacro: InitEvent;
  turn: Turn;
  questionsInv: InitQuestion[] = [];
  questionsFun: InitQuestion[] = [];
  questionsGoods: InitQuestion[] = [];
  questionsWork: InitQuestion[] = [];
  shareStock: SharesStock[] = [];
  loans: Loans[] = [];
  myInv: MyInvestments[] = [];
  personalInvestments: PersonalInvestments[] = [];
  myLoans: MyLoans[] = [];
  portfolioBack: Portfolio[] = [];
  endTurn: Button = {
    name: 'Cerrar sesión',
    innerName: 'endGame'
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
  myLoansTitle: ModalTab[] = [
    {
      name: 'Mis préstamos',
      active: true,
      internalName: 'myLoans',
      position: 0
    }
  ];
  question: ModalTab[] = [
    {
      name: 'Opción',
      active: true,
      internalName: 'questions',
      position: 0
    }
  ];

  constructor(
    private router: Router,
    private eventService: EventService,
    private questionsService: QuestionsService,
    private loanService: LoanService,
    private actionService: ActionsService,
    private turnService: InitTurnService
    ) { }

  ngOnInit(): void {
    this.initTurn(); // Init Event, Turn, Init Question
    // this.refreshTurn(); // Turn
    // this.questionSelected(); // Turn
    // this.catalogueActions(); // SharesStock
    // this.selectedAction(); // string Bien or error
    // this.catalogueLoan(); // Loan
    // this.selectedLoan(); // String Bien or error
    this.myInvestments(); //MyInvestments
    // this.investMoreMoney(); // string Bien or error
    // this.getMoneyfromAction(); // string error
    // this.sellAction(); // string Bien or error
    this.getOwnInvestment(); // PersonalInvestments
    // this.sellOwnInvestments(); // string Bien or error
    // this.seeMyLoans(); // MyLoans
    // this.reduceLoan(); // string error or Bien
    this.financialPortfolio(); // PortfolioBack
  }
  initTurn(): void {
    // this.eventService.initTurnEvent().subscribe(
    //   resp => {
    //     this.eventMicro = resp.filter((res: InitEvent) => res.TipoEvento === 'Micro')[0];
    //     this.eventMacro = resp.filter((res: InitEvent) => res.TipoEvento === 'Macro')[0];
    // }, error => {
    //   // TODO: Alert
    // });
    this.turnService.initTurn().subscribe(
      resp => {
        this.turn = resp[0];
      }, error => {
        //TODO: alert
    });
    this.questionsService.initTurnQuestions().subscribe(
      resp => {
        console.log(resp);
        this.questionsInv = resp.filter((r: InitQuestion) => r.TipoPregunta === 'Inversion');
        this.questionsGoods = resp.filter((r: InitQuestion) => r.TipoPregunta === 'Bienes Personales'); 
        this.questionsFun = resp.filter((r: InitQuestion) => r.TipoPregunta === 'Diversion'); 
        this.questionsWork = resp.filter((r: InitQuestion) => r.TipoPregunta === 'Laboral');
      }, error => {
        //TODO: alert
    });
  }
  refreshTurn(): void {
    this.turnService.refreshTurn().subscribe(
      resp => {
        this.turn = resp[0];
      }, error => {
        //TODO: alert
      }
    );
  }
  questionSelected(questionID: number): void {
    this.questionsService.questionSelected(questionID).subscribe(
      resp => {
        // console.log(resp);
        this.turn = resp[0];
      }, error => {
        //TODO: alert
      }
    );
  }
  catalogueActions(): void {
    this.actionService.getCatalogue().subscribe(
      resp => {
        this.shareStock = resp;
      }, error => {
        //TODO: alert
      }
    );
  }
  selectedAction(): void {
    this.actionService.investToNewAction(1, 1000).subscribe(
      resp => {
        window.alert(resp[0]);
      }, error => {
        //TODO: alert
      }
    );
  }
  catalogueLoan(): void {
    this.loanService.getCatalogue().subscribe(
      resp => {
        this.loans = resp;
      }, error => {
        //TODO: alert
      }
    );
  }
  selectedLoan(): void {
    this.loanService.selectedLoan(1, 2000, 200).subscribe(
      resp => {
        window.alert(resp);
      }, error => {
        //TODO: alert
      }
    );
  }
  myInvestments(): void {
    this.actionService.myActions().subscribe(
      resp => {
        // console.log(resp);
        this.myInv = resp; 
      }, error => {
        //TODO: alert
      }
    );
  }
  investMoreMoney(): void {
    this.actionService.investToOwnAction(3, 500).subscribe(
      resp => {
        window.alert(resp[0]);
      }, error => {
        //TODO: alert
      }
    );
  }
  getMoneyfromAction(): void {
    this.actionService.getMoneyFromAction(5, 1000).subscribe(
      resp => {
        window.alert(resp[0]);
      }, error => {
        //TODO: alert
      }
    );
  }
  sellAction(): void {
    this.actionService.sellAction(1).subscribe(
      resp => {
        window.alert(resp[0]);
      }, error => {
        //TODO: alert
      }
    );
  }
  getOwnInvestment(): void {
    this.actionService.myOwnInvestmentFromQuestions().subscribe(
      resp => {
        this.personalInvestments = resp;
        console.log(resp);
      }, error => {
        //TODO: alert
      }
    );
  }
  sellOwnInvestments(): void {
    this.actionService.sellOwnInvestments(1).subscribe(
      resp => {
        window.alert(resp[0]);
      }, error => {
        //TODO: alert
      }
    );
  }
  seeMyLoans(): void {
    this.loanService.seeMyLoans().subscribe(
      resp => {
        this.myLoans = resp;
      }, error => {
        //TODO: alert
      }
    );
  }
  reduceLoan(): void {
    this.loanService.payLoan(13, 500).subscribe(
      resp => {
        window.alert(resp[0]);
      }, error => {
        //TODO: alert
      }
    );
  }
  financialPortfolio(): void {
    this.turnService.financialPortfolio().subscribe(
      resp => {
        this.portfolioBack = resp;
      }, error => {
        //TODO: alert
      }
    );
  }
  close(action: boolean): void { // Notifications
    this.show = action;
  }
  closeGame(): void {
    localStorage.removeItem(KeysDataUser.userid);
    localStorage.removeItem(KeysDataUser.username);
    this.router.navigateByUrl('/');
  }
  openModalFun(activateModal: Button): void { // Modal
    switch(activateModal.innerName) {
      case 'portfolio': 
        this.dataTitle = this.portfolio;
        this.dataModal = this.portfolioBack;
        console.log(this.dataModal);
        break;
      case 'newActions':
        this.dataTitle = this.newActions;
        break;
      case 'newLoan':
        this.dataTitle = this.newLoan;
        break;
      case 'myActions':
        this.myInvestments();
        this.getOwnInvestment();
        this.dataModal = [{
          shared: this.myInv,
          own: this.personalInvestments
        }]
        this.dataTitle = this.myActions;
        break;
      case 'myLoans':
        this.dataTitle = this.myLoansTitle;
        break;
    }
    this.openModal = true;
  }
  modalActions(response: ModalResponse): void {
    switch(response.innerName) {
      case 'questions': 
        this.questionSelected(response.data[0].Pregunta_id);
        this.activeCards = false;
      break;
      // case 'newActions':
      //   this.dataTitle = this.newActions;
      //   break;
      // case 'newLoan':
      //   this.dataTitle = this.newLoan;
      //   break;
      // case 'myActions':
      //   this.dataTitle = this.myActions;
      //   break;
      // case 'myLoans':
      //   this.dataTitle = this.myLoansTitle;
      //   break;
    }
    this.openModal = response.flag;
  }
  openModalCard(question: InitQuestion): void { 
    this.dataModal = [question];
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
  cancelModal(): void {
    this.openModal = false;
  }
}

