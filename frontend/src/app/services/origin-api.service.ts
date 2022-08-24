import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { createHash } from 'crypto';

@Injectable({
  providedIn: 'root'
})
export class OriginAPIService {
  

  constructor(private httpClient: HttpClient) { }

  register(username: string, email: string, password: string){
    const url =  'http://127.0.0.1:5000/register'
    password = createHash('sha128').update(password).digest('hex');
    console.log(password);
    return this.httpClient.post(url, {"username": username, "email": email, "password": password})
  }
}
