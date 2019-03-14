import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { OkCancelComponent } from './ok-cancel.component';

describe('OkCancelComponent', () => {
  let component: OkCancelComponent;
  let fixture: ComponentFixture<OkCancelComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ OkCancelComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(OkCancelComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
