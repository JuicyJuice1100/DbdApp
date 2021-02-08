import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { MyBuildsPageRoutingModule } from './my-builds-routing.module';

import { MyBuildsPage } from './my-builds.page';

import { BuildContainerComponent } from '../build-container/build-container.component';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    MyBuildsPageRoutingModule,
  ],
  declarations: [MyBuildsPage, BuildContainerComponent]
})
export class MyBuildsPageModule {}
