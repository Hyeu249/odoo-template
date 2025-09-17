import { Component, xml, useState } from "@odoo/owl";

import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";

export class Balance extends Component {
  static props = [];
  static template = xml`
        <div style="display: flex; align-items: center; gap: 8px; background-color: white; padding: 5px 15px; border-radius: 5px; margin: auto;">
            <i class="fa fa-credit-card" aria-hidden="true"></i> Số dư: <span id="balance"><t t-esc="state.balance"/>đ</span>
            <span class="reload-icon" t-att-class="{'loading': state.loading}" t-on-click="fetchBankModel"><i class="fa fa-refresh"/></span>
        </div>
    `;

  setup() {
    super.setup();
    this.state = useState({ balance: 100 });
    this.orm = useService("orm");

    this.fetchBankModel();
  }

  async fetchBankModel() {

  }
}

registry
  .category("systray")
  .add("balance", { Component: Balance }, { sequence: 100 });
