import { TestBed } from '@angular/core/testing';

import { OriginAPIService } from './origin-api.service';

describe('OriginAPIService', () => {
  let service: OriginAPIService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(OriginAPIService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
