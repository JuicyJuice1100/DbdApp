import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-build-container',
  templateUrl: './build-container.component.html',
  styleUrls: ['./build-container.component.scss'],
})
export class BuildContainerComponent implements OnInit {
  @Input() builds: any;

  constructor() { }

  ngOnInit() {}

}
