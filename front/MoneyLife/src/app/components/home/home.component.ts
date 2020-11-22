import { Component, OnInit } from '@angular/core';
import { KeysDataUser } from 'src/app/auth/keys-data';
import { Router } from '@angular/router';
/** Services */
import { EventService } from 'src/app/events-news/services/event.service';
import { QuestionsService } from 'src/app/flip-card/services/questions.service';
import { LoanService } from 'src/app/loan/services/loan.service';
import { ActionsService } from '../services/actions.service';
import { InitTurnService } from '../services/turn.service';
import { HappinessService } from 'src/app/happiness/services/happiness.service';
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
import { Happiness } from 'src/app/happiness/interfaces/happiness';


@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {
  show = false;
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
  myInv: MyInvestments[] = [];

  microEvent: ModalTab[] = [
    {
      name: 'Evento Micro',
      active: true,
      internalName: 'microEvent',
      position: 0
    }
  ];
  happiness: ModalTab[] = [
    {
      name: 'Felicidad',
      active: true,
      internalName: 'happiness',
      position: 0
    }
  ];
  endTurnBtn: Button = {
    name: 'Salir',
    innerName: 'endGame'
  }
  endTurn: ModalTab[] = [
    {
      name: 'Salir',
      active: true,
      internalName: 'endGame',
      position: 0
    }
  ];
  portfolioBtn: Button = {
    name: 'Flujo de efectivo',
    innerName: 'portfolio'
  };
  portfolio: ModalTab[] = [
    {
      name: 'Flujo de efectivo',
      active: true,
      internalName: 'portfolio',
      position: 0
    }
  ]
  newActionsBtn: Button = {
    name: 'Inversión en bolsa',
    innerName: 'newActions',
  };
  newActions: ModalTab[] = [
    {
      name: 'Inversión en bolsa',
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
      name: 'Inversión en bolsa',
      active: true,
      internalName: 'myActions',
      position: 0
    },
    {
      name: 'Personales',
      active: false,
      internalName: 'myActions',
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
    private turnService: InitTurnService,
    private happinessService: HappinessService
    ) { }

  ngOnInit(): void {
    this.initTurn(); // Init Event, Turn, Init Question DEJAR
  }
  initTurn(): void {
    this.eventService.initTurnEvent().subscribe(
      resp => {
        if (resp) {
          const micro = resp.filter((res: InitEvent) => res.TipoEvento === 'Micro')[0] as InitEvent;
          const macro = resp.filter((res: InitEvent) => res.TipoEvento === 'Macro')[0] as InitEvent;
          if (micro) {
            this.eventMicro = micro;
            this.show = true;
          } else {
            this.eventMicro = null;
            this.show = false;
          }
          this.eventMacro = (macro) ? macro : null;
          this.turnService.initTurn().subscribe(
            resp => {
              this.turn = resp[0];
            }, error => {
              //TODO: alert
          });
        }
    }, error => {
      // TODO: Alert
    });

    this.questionsService.initTurnQuestions().subscribe(
      resp => {
        this.questionsInv = resp.filter((r: InitQuestion) => r.TipoPregunta === 'Inversion');
        this.questionsGoods = resp.filter((r: InitQuestion) => r.TipoPregunta === 'Bienes Personales'); 
        this.questionsFun = resp.filter((r: InitQuestion) => r.TipoPregunta === 'Diversion'); 
        this.questionsWork = resp.filter((r: InitQuestion) => r.TipoPregunta === 'Laboral');
        this.activeCards = true;
      }, error => {
        //TODO: alert
    });
  }
  refreshTurn(): void {
    this.turnService.refreshTurn().subscribe(
      resp => {
        this.turn = resp[0] as Turn;
      }, error => {
        //TODO: alert
      }
    );
  }
  questionSelected(questionID: number): void {
    this.questionsService.questionSelected(questionID).subscribe(
      resp => {
        if (resp.mensaje) {
          window.alert(resp.mensaje);
        } else {
          // this.turn = resp[0] as Turn;
          this.refreshTurn();
          this.activeCards = false;
        }
      }, error => {
        //TODO: alert
      }
    );
  }
  catalogueActions(): void {
    this.actionService.getCatalogue().subscribe(
      resp => {
        this.dataModal = resp as SharesStock[];
        this.dataTitle = this.newActions;
        this.openModal = true;
      }, error => {
        //TODO: alert
      }
    );
  }
  selectedAction(actionID: number, qty: number): void {
    this.actionService.investToNewAction(actionID, qty).subscribe(
      resp => {
        window.alert(resp.mensaje);
        this.refreshTurn();
      }, error => {
        //TODO: alert
      }
    );
  }
  catalogueLoan(): void {
    this.loanService.getCatalogue().subscribe(
      resp => {
        this.dataModal = resp as Loans[];
        this.dataTitle = this.newLoan;
        this.openModal = true;
      }, error => {
        //TODO: alert
      }
    );
  }
  selectedLoan(loanID: number, totalValue: number, hitch: number): void {
    this.loanService.selectedLoan(loanID, totalValue, hitch).subscribe(
      resp => {
        window.alert(resp.mensaje);
        this.refreshTurn();
      }, error => {
        //TODO: alert
      }
    );
  }
  myInvestments(): void {
    this.actionService.myActions().subscribe(
      resp => {
        this.myInv = resp as MyInvestments[]; 
        this.getOwnInvestment();
      }, error => {
        //TODO: alert
      }
    );
  }
  investMoreMoney(actionID: number, qty: number): void {
    this.actionService.investToOwnAction(actionID, qty).subscribe(
      resp => {
        window.alert(resp.mensaje);
        this.refreshTurn();
      }, error => {
        //TODO: alert
      }
    );
  }
  getMoneyfromAction(actionID: number, qty: number): void {
    this.actionService.getMoneyFromAction(actionID, qty).subscribe(
      resp => {
        window.alert(resp.mensaje);
        this.refreshTurn();
      }, error => {
        //TODO: alert
      }
    );
  }
  sellAction(actionID: number): void {
    this.actionService.sellAction(actionID).subscribe(
      resp => {
        window.alert(resp.mensaje);
        this.refreshTurn();
      }, error => {
        //TODO: alert
      }
    );
  }
  getOwnInvestment(): void {
    this.actionService.myOwnInvestmentFromQuestions().subscribe(
      resp => {
        this.dataModal = [{
          shared: this.myInv as MyInvestments[],
          own: resp as PersonalInvestments[]
        }];
        this.dataTitle = this.myActions;
        this.openModal = true;
      }, error => {
        //TODO: alert
      }
    );
  }
  sellOwnInvestments(actionID: number): void {
    this.actionService.sellOwnInvestments(actionID).subscribe(
      resp => {
        window.alert(resp.mensaje);
        this.refreshTurn();
      }, error => {
        //TODO: alert
      }
    );
  }
  seeMyLoans(): void {
    this.loanService.seeMyLoans().subscribe(
      resp => {
        this.dataModal = resp as MyLoans[];
        this.dataTitle = this.myLoansTitle;
        this.openModal = true;
      }, error => {
        //TODO: alert
      }
    );
  }
  reduceLoan(loanID: number, qty: number): void {
    this.loanService.payLoan(loanID, qty).subscribe(
      resp => {
        window.alert(resp.mensaje);
        this.refreshTurn();
      }, error => {
        //TODO: alert
      }
    );
  }
  financialPortfolio(): void {
    this.turnService.financialPortfolio().subscribe(
      resp => {
        this.dataModal = resp as Portfolio[];
        this.dataTitle = this.portfolio;
        this.openModal = true;
      }, error => {
        //TODO: alert
      }
    );
  }
  showHappiness(): void {
    this.happinessService.getHappiness().subscribe(
      resp => {
        this.dataModal = resp as Happiness[];
        this.dataTitle = this.happiness;
        this.openModal = true;
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
        this.financialPortfolio();
        break;
      case 'newActions':
        this.catalogueActions();
        break;
      case 'newLoan':
        this.catalogueLoan();
        break;
      case 'myActions':
        this.myInvestments();
        break;
      case 'myLoans': 
        this.seeMyLoans();
        break;
      case 'endGame':
        this.dataTitle = this.endTurn;
        this.openModal = true;
        break;
      case 'microEvent':
        this.dataModal = [this.eventMicro];
        this.dataTitle = this.microEvent;
        this.openModal = true;
        break;
    }
  }
  modalActions(response: ModalResponse): void {
    switch(response.innerName) {
      case 'questions': 
        this.questionSelected(response.data[0].Pregunta_id);
        break;
      case 'newActions':
        this.selectedAction(response.data.id, response.qty);
        break;
      case 'newLoan':
        this.selectedLoan(response.data.id, response.qty, response.hitch);
        break;
      case 'myActionsSell':
        this.sellAction(response.data.id);
        break;
      case 'myActionsgetMoney':
        this.getMoneyfromAction(response.data.id, response.hitch);
        break;
      case 'myActionsinvest':
        this.investMoreMoney(response.data.id, response.qty);
        break;
      case 'myActionsPersonal':
        this.sellOwnInvestments(response.data.id);
        break;
      case 'myLoans':
        this.reduceLoan(response.data.PrestamoID, response.qty);
        break;
      case 'endGameSave':
        this.closeGame();
        break;
      case 'endGameErase':
        this.turnService.eraseGame().subscribe(
          resp => {
            this.closeGame();
          }, error => {
            // alert
          });
        break;
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

