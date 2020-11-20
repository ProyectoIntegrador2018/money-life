import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { LoginService } from 'src/app/services/login.service'; //Llamar servicio de login

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
  register; //Variable para guardar input de usuario
  inputLogin; //Variable para login

  constructor(private loginService : LoginService) { }

  ngOnInit(): void {
    this.initForm();
    this.register = {
      username: '',
      password: '' 
    };
    this.inputLogin = {
      username: '',
      password: ''  
    };
  }
  initForm(): void {
    this.logInForm = new FormGroup({
      user: new FormControl('', [
        Validators.required,
        Validators.pattern('^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$')
      ]),
      password: new FormControl('',
      [Validators.required])
    });
    this.registerForm = new FormGroup({
      newUser: new FormControl('', [
        Validators.required,
        Validators.pattern('^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$')
      ]),
      newPassword: new FormControl('', [
        Validators.required]),
      newPassword2: new FormControl('',[
        Validators.required]),
    });
    this.recoverForm = new FormGroup({
      recoverEmail: new FormControl('', [
        Validators.required,
        Validators.pattern('^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$')
      ])});
  }

  onSubmit(): void {
    console.log(this.logInForm.status);
    if (this.logInForm.status === 'VALID') {
      // TODO: call services to make log in
      this.inputLogin.username = this.logInForm.controls.user.value
      this.inputLogin.password = this.logInForm.controls.password.value

      this.loginService.onLogin(this.inputLogin).subscribe(
        (resp) => {
          console.log(resp);
        },
        (error) => console.log('error', error)
      );

    } else {
      if (this.logInForm.controls.user.status === 'INVALID') {
        this.errorUser = true;
      }
      if (this.logInForm.controls.password.status === 'INVALID') {
        this.errorPass = true;
      }
    }
  }
  onSubmitRegister(): void {
    if (this.registerForm.status === 'VALID') {
      // TODO: call services to make registration
      this.register.username = this.registerForm.controls.newUser.value
      this.register.password = this.registerForm.controls.newPassword.value

      this.loginService.postRegister(this.register).subscribe(
        (resp) => {
          console.log('Se creo '+ this.register.username)
        },
        (error) => console.log('error', error)
      );
    } else {
      if (this.registerForm.controls.newUser.status === 'INVALID') {
        this.errorUserNew = true;
      }
      if (this.registerForm.controls.newPassword.status === 'INVALID') {
        this.errorPassNew = true;
      }
      if (this.registerForm.controls.newPassword2.status === 'INVALID') {
        this.errorPassNew2 = true;
      }
    }
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
