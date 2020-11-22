import { Affects } from 'src/app/shared/interfaces/affects';

export interface InitEvent {
    Descripcion?: string;
    Evento_id?: number;
    TipoEvento?: string;
    Afecta: Affects[]
}
