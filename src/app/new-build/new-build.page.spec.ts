import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { NewBuildPage } from './new-build.page';

describe('NewBuildPage', () => {
  let component: NewBuildPage;
  let fixture: ComponentFixture<NewBuildPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ NewBuildPage ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(NewBuildPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
