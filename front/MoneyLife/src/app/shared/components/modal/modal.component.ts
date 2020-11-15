import { Component, EventEmitter, Input, OnInit, Output, HostListener, OnChanges } from '@angular/core';
import { ModalTab } from '../../interfaces/modal-tab';

@Component({
  selector: 'app-modal',
  templateUrl: './modal.component.html',
  styleUrls: ['./modal.component.scss']
})
export class ModalComponent implements OnInit, OnChanges {
  @Input() open: boolean;
  @Input() titles: ModalTab[];
  @Output() close: EventEmitter<boolean> = new EventEmitter<boolean>();
  lastActive = 0;
  activeSwitch: ModalTab;
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

  closeModal(): void {
    this.open = false;
    this.close.emit(false);
  }
  changeTab(tab: ModalTab): void {
    if(this.titles[this.lastActive]) {
      this.titles[this.lastActive].active = false;
      this.titles[tab.position].active = true;
      this.lastActive = tab.position;
      this.activeSwitch = tab;
    }
  }

  @HostListener('document:keyup.escape', ['$event'])
  onEscape() {
    this.closeModal();
  }
}
