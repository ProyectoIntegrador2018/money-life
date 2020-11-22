import { Component, EventEmitter, Input, OnInit, Output, HostListener, OnChanges } from '@angular/core';
import { ModalTab } from 'src/app/shared/interfaces/modal-tab';
import { ModalResponse } from 'src/app/shared/interfaces/modal-response';

@Component({
  selector: 'app-modal',
  templateUrl: './modal.component.html',
  styleUrls: ['./modal.component.scss']
})
export class ModalComponent implements OnInit, OnChanges {
  @Input() open: boolean;
  @Input() titles: ModalTab[];
  @Input() data: any[];
  @Output() close: EventEmitter<ModalResponse> = new EventEmitter<ModalResponse>();
  @Output() cancelModal: EventEmitter<boolean> = new EventEmitter<boolean>();
  lastActive = 0;
  activeSwitch: ModalTab;
  sendData: ModalResponse;
  dt: any;
  qty: number;
  hitch: number;
  selected = false;
  objSelected: any;
  constructor() { }

  ngOnInit(): void {
  }
  ngOnChanges(): void {
    if (this.titles) {
      const aux = this.titles.filter(t => t.active);
      this.lastActive = aux[0].position;
      this.activeSwitch = aux[0];
    }
  }

  closeModal(): void { // Mandar informacion mas que nada en preguntas
    this.open = false;
    this.sendData = {
      innerName: this.activeSwitch.internalName,
      data: this.data,
      qty: this.qty,
      flag: false
    }
    this.close.emit(this.sendData);
  }
  changeTab(tab: ModalTab): void { // Cambiar tab
    if(this.titles[this.lastActive]) {
      this.titles[this.lastActive].active = false;
      this.titles[tab.position].active = true;
      this.lastActive = tab.position;
      this.activeSwitch = tab;
      this.cancelObj();
    }
  }

  cancelModalFunc(): void { // Cancelar modal sin mandar info
    this.cancelModal.emit(false);
  }
  cancelObj(): void { // Cancela objeto unico
    this.objSelected = null;
    this.selected = false;
  }
  selectedObj(obj: any): void { // Marcar opcion seleccionada para hacer algo con ella
    this.objSelected = obj;
    this.selected = true;
  }
  sendSelectedObj(action: string): void { // Mandar informacion con opcion seleccionada
    this.sendData = {
      innerName: action,
      data: this.objSelected,
      qty: this.qty,
      hitch: this.hitch,
      flag: false
    }
    this.close.emit(this.sendData);
  }
  @HostListener('document:keyup.escape', ['$event'])
  onEscape() {
    this.cancelModalFunc();
  }
}
