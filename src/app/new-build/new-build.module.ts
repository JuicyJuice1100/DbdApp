import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { NewBuildPageRoutingModule } from './new-build-routing.module';

import { NewBuildPage } from './new-build.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    NewBuildPageRoutingModule
  ],
  declarations: [NewBuildPage]
})
export class NewBuildPageModule {}
