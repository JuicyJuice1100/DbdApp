import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { MyBuildsPage } from './my-builds.page';

describe('MyBuildsPage', () => {
  let component: MyBuildsPage;
  let fixture: ComponentFixture<MyBuildsPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MyBuildsPage ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(MyBuildsPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
