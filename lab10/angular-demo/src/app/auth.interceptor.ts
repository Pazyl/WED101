import { Observable } from 'rxjs/internal/Observable';
import { Injectable } from '@angular/core';
import { HttpEvent, HttpHandler, HttpInterceptor, HttpRequest } from '@angular/common/http';

@Injectable()
export class AuthInterceptor implements HttpInterceptor {

  constructor() {}

  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {

    const token = localStorage.getItem('token');
    if (token){
      const authReq = req.clone({
        headers: req.headers.append('Authorization', `JWT ${token}`)
      });
      return next.handle(authReq);
    }

    return next.handle(req);
  }
}
