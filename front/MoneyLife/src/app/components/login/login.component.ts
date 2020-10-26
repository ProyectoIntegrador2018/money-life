import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
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
  constructor() { }

  ngOnInit(): void {
    this.initForm();
    
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
