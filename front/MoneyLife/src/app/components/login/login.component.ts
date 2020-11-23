import { FormGroup, FormControl, Validators } from '@angular/forms';
import { Component, OnInit  } from '@angular/core';
import { LoginService } from '../services/login.service';
import { KeysDataUser } from 'src/app/auth/keys-data';
import { User } from '../interfaces/user';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss'],
  providers: [LoginService]  //Provedor login
})
export class LoginComponent implements OnInit {
  action = 'login';
  logInForm: FormGroup;
  registerForm: FormGroup;
  recoverForm: FormGroup;
  errorUser = false;
  errorPass = false;
  errorUserNew = false;
  errorPassNew = false;
  errorPassNew2 = false;
  errorRecover = false;
  constructor(
    private loginService: LoginService,
    private router: Router,
    ) { }

  ngOnInit(): void {
    this.initForm();
  }
  initForm(): void {
    this.logInForm = new FormGroup({
      username: new FormControl('', [
        Validators.required,
        Validators.pattern('^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$')
      ]),
      password: new FormControl('',
      [Validators.required])
    });
    this.registerForm = new FormGroup({
      username: new FormControl('', [
        Validators.required,
        Validators.pattern('^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$')
      ]),
      password: new FormControl('', [
        Validators.required]),
      password2: new FormControl('',[
        Validators.required],
        ),
    });
    this.recoverForm = new FormGroup({
      recoverEmail: new FormControl('', [
        Validators.required,
        Validators.pattern('^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$')
      ])});
  }

  onSubmit(): void {
    if (this.logInForm.status === 'VALID') {

      this.loginService.login(this.logInForm.value).subscribe(
        resp => {
          if(resp.mensaje) {
            window.alert(resp.mensaje);
          } else {
            this.setUser(resp as User);
          }
        }, error => {
          //TODO: Alert error
        }
      );
    } else {
      if (this.logInForm.controls.username.status === 'INVALID') {
        this.errorUser = true;
      }
      if (this.logInForm.controls.password.status === 'INVALID') {
        this.errorPass = true;
      }
    }
  }
  onSubmitRegister(): void {
    if (this.registerForm.controls.password.value === this.registerForm.controls.password2.value) {
      if (this.registerForm.status === 'VALID') {
        this.loginService.register(this.registerForm.value).subscribe(
          resp => {
            this.setUser(resp as User);
          }, error => {
            window.alert('El usuario ya existe');
            console.log('error', error);
          }
        );
      } else {
        if (this.registerForm.controls.username.status === 'INVALID') {
          this.errorUserNew = true;
        }
        if (this.registerForm.controls.password.status === 'INVALID') {
          this.errorPassNew = true;
        }
        if (this.registerForm.controls.password2.status === 'INVALID') {
          this.errorPassNew2 = true;
        }
      }
    } else {
      this.errorPassNew = true;
      this.errorPassNew2 = true;
    }
  }

  setUser(user: User): void {
    localStorage.setItem(KeysDataUser.userid,  user.id.toString());
    localStorage.setItem(KeysDataUser.username, user.username);
    this.router.navigateByUrl("/game");
  }
  onSubmitRecover(): void {
    if (this.recoverForm.status === 'VALID') {
      // TODO: call services to recover password
    } else {
      this.errorRecover = true;
    }
  }

  resetAll(): void {
    this.logInForm.reset();
    this.recoverForm.reset();
    this.registerForm.reset();
    this.errorPass = false;
    this.errorPassNew = false;
    this.errorPassNew2 = false;
    this.errorRecover = false;
    this.errorUser = false;
    this.errorUserNew = false;
  }
}
