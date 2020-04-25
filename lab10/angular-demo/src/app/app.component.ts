import { Component, OnInit } from '@angular/core';
import { ControlDataService } from './control-data.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'Pazyll';

  logged = false;

  username = '';
  password = '';

  constructor(private service: ControlDataService) {}

  ngOnInit(){
    let token = localStorage.getItem('token');
    if (token){
      this.logged = true;
    }
  }

  login(){
    this.service.login(this.username, this.password)
      .subscribe(res => {
        localStorage.setItem('token', res.token);
        this.logged = true;
        this.username = '';
        this.password = '';
      });
  }

  logout(){
    localStorage.clear();
    this.logged = false;
  }

}
